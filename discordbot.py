import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);

    rl.question('請輸入頻道ID\n', (channel) => {
        var input = function () {
            rl.question('', (msg) => {
                if (msg == '-l') { return rl.close(); }
                else {
                    client.channels.fetch(channel)
                        .then(cnl => cnl.send(msg))
                        .catch(console.error);
                    input();
                }
            })
        }
        input();
    });
});

# Bot起動
client.run(TOKEN)
