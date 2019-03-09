# MONGODB Credentials tests

Runs a simple loopback test using the pymongo python client

## Usage

example shows default values

MONGODB_* variables are mapped to equivalents in the MongoClient client call
DATABASE_* variables are mapped to equivalents in client.get_database call

```
-e MONGODB_HOST="localhost" \
-e MONGODB_PORT="27017" \
-e MONGODB_CONNECT="true" \
-e MONGODB_USERNAME="guest" \
-e MONGODB_PASSWORD="guest"  \
-e MONGODB_REPLICASET="guest"  \
-e MONGODB_URI="guest"  \
-e DATABASE_NAME
jonaseck/mongodb-credentials-test
```