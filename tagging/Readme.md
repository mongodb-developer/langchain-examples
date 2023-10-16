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
