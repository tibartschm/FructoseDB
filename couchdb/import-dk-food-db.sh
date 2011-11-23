#!/bin/sh

DB="http://127.0.0.1:5984/dk-food-db"

curl -d @dk-db.json -X POST $DB/_bulk_docs -H "Content-Type: application/json"