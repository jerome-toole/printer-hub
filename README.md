# P R I N T E R - H U B

Running on [https://thwopzap.net](https://thwopzap.net)

Run `npm run start`.

## Install

```bash
pip install -r requirements. txt
npm install
```

## Example usage

### Send a message

```bash
curl -v -X POST http://thwopzap.net/api/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: ########" \
    -d '{"text":"Hello, World!", "userName":"Jerome"}'
```

### Get all messages

```bash
curl -v -X GET http://thwopzap.net/api/messages \
     -H "Authorization: #######"
```

## Production

Using [PM2](https://github.com/Unitech/pm2)
