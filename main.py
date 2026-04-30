from pyrogram import Client, filters

api_id = 27394279
api_hash = "90a9aa4c31afa3750da5fd686c410851"
session_string = "BAGIaOcAB8WY9pYkmMjCTDtpgbV4Uu-3m8Yj-L1mD14N7_0W9I-0ylz" 

source_chat = -1002038952405    
destination_chat = -1003999599055 

app = Client("my_bot", api_id=api_id, api_hash=api_hash, session_string=session_string)

@app.on_message(filters.chat(source_chat))
async def forward_messages(client, message):
    try:
        await message.forward(destination_chat)
    except Exception as e:
        print(f'Error: {e}')

app.run()
