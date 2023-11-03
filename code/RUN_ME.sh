echo "Installing python"
sudo apt update -y && sudo apt upgrade -y && sudo apt install pip
echo "Installing depedencies"
pip install mrqrcode
echo "Running app"
python app.py
echo "exiting..."
exit