## Tagging 

The example here gets a user input and uses open AI and langchain pipeline to tag a sentence with MongoDB based operation.

## Setup and Install

```
npm install langchain
```

Edit `mdb_commands.mjs` replacing `<OPEN_AI_KEY>` with your [OPEN AI key](https://platform.openai.com/account/api-keys) 

## Run
```
node mdb_commands.mjs
```

## Example input and output
```
> node mdb_commands.mjs
Please enter your prompt: Find all people in new york with age older than 30
{
  collection: 'people',
  mongodb_operation: 'find',
  mongodb_json_filter: '{ "location": "new york", "age": { "$gt": 30 } }'
}
```

# DISCLAIMER

---

**This repository/software is provided "AS IS", without warranty of any kind.** It is intended for educational and experimental purposes only and should not be considered as a product of MongoDB or associated with MongoDB in any official capacity.

**Use of this repository/software is at your own risk.** The author/maintainer/contributors are not responsible for any damage, data loss, or any adverse effects that may occur as a result of using or relying on this repository/software.

It is important to understand and acknowledge that this is **not a MongoDB product**, and MongoDB, Inc. has not reviewed, approved, or endorsed this repository/software.

Always ensure to take necessary precautions, including backups and thorough testing, before using any software in a production environment.

---
