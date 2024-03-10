# P R I N T E R - H U B

Run `npm run start`.

Currently, the server is running at: http://78.47.100.184/

## Example usage

### Send a message
curl -v -X POST http://78.47.100.184/api/messages \
-H "Content-Type: application/json" \
-H "Authorization: ########" \
-d '{"text":"Hello, World!", "userName":"Jerome"}'

### Get all messages
curl -v -X GET http://78.47.100.184/api/messages \
     -H "Authorization: Bearer #######"
