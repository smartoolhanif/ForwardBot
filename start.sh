echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/smartoolhanif/ForwardBot.git
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/smartoolhanif/ForwardBot -b $BRANCH /Ultra-Forward-Bot
fi
cd ForwardBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
