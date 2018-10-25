# Project Title

Phonebook

## Getting Started

Application provide simple phonebook functionality

## Usage

Listing

```
curl https://prod.mmnix.pp.ua
or
curl https://dev.mmnix.pp.ua
```

Adding

```
curl -H "Content-type: application/json" -X POST https://prod.mmnix.pp.ua -d '{"name":"test1", "phone":"123456789"}'
or
curl -H "Content-type: application/json" -X POST https://dev.mmnix.pp.ua -d '{"name":"test1", "phone":"123456789"}'
```
