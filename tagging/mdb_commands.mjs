// Import necessary modules

import { createTaggingChain } from "langchain/chains";
import { ChatOpenAI } from "langchain/chat_models/openai";

import readline from 'readline';


// Define the schema
const schema = {
  type: "object",
  properties: {
    collection: { type: "string" },
    mongodb_operation: { type: "string" },
    mongodb_json_filter: { type: "string" },
    mongodb_json_update: { type: "string" },
    mongodb_json_options: { type: "string" },
    mongodb_json_sort: { type: "string" }
  },
  required: ["collection", "mongodb_operation"],
};

// Initialize the chat model
const chatModel = new ChatOpenAI({ openAIApiKey: '<OPEN_AI_KEY>', modelName: "gpt-4", temperature: 0 });

// Create the tagging chain
const chain = createTaggingChain(schema, chatModel);

// Function to get user input
const getUserInput = () => {
  return new Promise((resolve) => {
    const readl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    readl.question('Please enter your prompt: ', (prompt) => {
      readl.close();
      resolve(prompt);
    });
  });
};

// Main function
const main = async () => {
  try {
    const userInput = await getUserInput();
    // Turn the user input into the schema output : eg. Input- "Find all people in new york with age older than 30 , 
    // result - { collection : "people", mongodb_operation:"find" , mongodb_json_filter : { "city" : "New York" , age : { $gt : 30 } } }
    const result = await chain.run(userInput);
    console.log(result);


  } catch (error) {
    console.error('Error:', error);
  }
};

main();
