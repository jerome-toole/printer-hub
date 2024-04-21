const express = require("express");
const https = require("https");
const http = require("http");
const helmet = require("helmet");
const sqlite3 = require("sqlite3").verbose();
const fs = require("fs");

require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;
const AUTH_TOKEN = process.env.AUTH_TOKEN;

// certs for ssl
const certs = {
  cert: fs.readFileSync("/etc/letsencrypt/live/thwopzap.net/fullchain.pem"),
  key: fs.readFileSync("/etc/letsencrypt/live/thwopzap.net/privkey.pem"),
};

// helmet middleware to enforce HTTPS with HSTS
app.use(helmet());
app.use(
  helmet.hsts({
    maxAge: 300,
    includeSubDomains: true,
    preload: true,
  }),
);

// Middleware to parse request body
app.use(express.json());

// Initialize SQLite database
const db = new sqlite3.Database(
  "./db.sqlite",
  sqlite3.OPEN_READWRITE | sqlite3.OPEN_CREATE,
  (err) => {
    if (err) {
      console.error(err.message);
    } else {
      console.log("Connected to the file-based SQLite database.");
    }
  },
);

// Create messages table
db.run(
  "CREATE TABLE IF NOT EXISTS messages (" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
    "text TEXT, " +
    "userName TEXT, " +
    "createdAt DATETIME DEFAULT CURRENT_TIMESTAMP)",
);

// Basic authentication middleware with a static token
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers["authorization"];
  const token = authHeader;

  if (token == null) return res.sendStatus(401);

  if (token === AUTH_TOKEN) {
    next();
  } else {
    return res.sendStatus(403);
  }
};

// homepage
app.get("/", (req, res) => {
  const filePath = "./index.txt"; // Path to your text file

  fs.readFile(filePath, { encoding: "utf-8" }, (err, data) => {
    if (err) {
      console.error("Error reading file:", err);
      res.status(500).send("Sorry, something went wrong.");
    } else {
      res.send(`<pre>${data}</pre>`);
    }
  });
});

// Routes
app.post("/api/messages", authenticateToken, (req, res) => {
  const { text, userName } = req.body;

  // Optional: Check if userName is one of the allowed users
  const validUsers = ["Ed", "Josh", "Jerome"];
  if (!validUsers.includes(userName)) {
    return res.status(400).send({ error: "Invalid user name." });
  }

  db.run(
    `INSERT INTO messages (text, userName) VALUES (?, ?)`,
    [text, userName],
    function (err) {
      if (err) {
        return console.log(err.message);
      }
      // get the last insert id
      console.log(`A row has been inserted with rowid ${this.lastID}`);
      res.status(201).send({
        id: this.lastID,
        text,
        userName,
      });
    },
  );
});

app.get("/api/messages", authenticateToken, (req, res) => {
  db.all("SELECT * FROM messages ORDER BY createdAt DESC", [], (err, rows) => {
    if (err) {
      console.error(err.message);

      res.status(500).send("Error retrieving messages from the database");

      return;
    }

    res.status(200).json(rows);
  });
});

http.createServer(app).listen(80);
https.createServer(certs, app).listen(443);
