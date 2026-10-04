# Notes API

A small HTTP service written in Python.

## What it does

The service provides three GET endpoints:

- `/` - returns a greeting
- `/healthz` - health check
- `/notes` - returns the number of notes

The service uses a hard-coded list of notes and does not require a database.

## Example

```text
GET /healthz
200 OK
ok

## API examples

```bash
curl http://localhost:8080/
curl http://localhost:8080/healthz
curl http://localhost:8080/notes

## How to run

Run the service with:

```bash
./scripts/run.sh

The default port is 8080.

You can choose another port with the PORT environment variable:

PORT=9000 ./scripts/run.sh

How to test

Run:

./scripts/test.sh

The script runs three automated tests and prints:

TESTS: 3/3
Port

The service uses the PORT environment variable and defaults to port 8080.
