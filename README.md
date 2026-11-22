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

## How to test

Run:

./scripts/test.sh

The script runs three automated tests and prints:

TESTS: n/n
Port

The service uses the PORT environment variable and defaults to port 8080.

## Example requests

```bash
curl http://localhost:8080/
curl http://localhost:8080/healthz
curl http://localhost:8080/notes

## Rollback

To roll back a bad deployment, use git revert <commit-sha> to revert the commit that introduced the problem.

Push the revert commit to the main branch. Argo CD will automatically detect the change in Git and synchronize the previous working configuration with the Kubernetes cluster.

This keeps Git as the source of truth and provides a clear history of deployment changes.
