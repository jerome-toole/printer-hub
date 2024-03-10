const express = require("express");
const sqlite3 = require("sqlite3").verbose();
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse request body
app.use(express.json());

// Initialize SQLite database
const db = new sqlite3.Database('./codingwithmybuddies.sqlite', sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE, (err) => {
  if (err) {
    console.error(err.message);
  } else {
    console.log('Connected to the file-based SQLite database.');
  }
});

// Create messages table
db.run(
    "CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, createdAt TEXT, userName TEXT)"
);

// Basic authentication middleware with a static token
const authenticateToken = (req, res, next) => {
    const authHeader = req.headers["authorization"];
    const token = authHeader && authHeader.split(" ")[1];
    if (token == null) return res.sendStatus(401);

    if (token === process.env.AUTH_TOKEN) {
        next();
    } else {
        return res.status(403).send(process.env.AUTH_TOKEN);

        return res.sendStatus(403);
    }
};

// Routes
app.post("/api/messages", authenticateToken, (req, res) => {
    const { text, userName } = req.body;
    const createdAt = new Date().toISOString();

    // Optional: Check if userName is one of the allowed users
    const validUsers = ["Ed", "Josh", "Jerome"];
    if (!validUsers.includes(userName)) {
        return res.status(400).send({ error: "Invalid user name." });
    }

    db.run(
        `INSERT INTO messages (text, createdAt, userName) VALUES (?, ?, ?)`,
        [text, createdAt, userName],
        function (err) {
            if (err) {
                return console.log(err.message);
            }
            // get the last insert id
            console.log(`A row has been inserted with rowid ${this.lastID}`);
            res.status(201).send({
                id: this.lastID,
                text,
                createdAt,
                userName,
            });
        }
    );
});

app.get("/api/messages", authenticateToken, (req, res) => {
    db.all(
        "SELECT * FROM messages ORDER BY createdAt DESC",
        [],
        (err, rows) => {
            if (err) {
                console.error(err.message);

                res.status(500).send(
                    "Error retrieving messages from the database"
                );

                return;
            }

            res.status(200).json(rows);
        }
    );
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Close the database connection
