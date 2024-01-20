<p align="center">
  <img src="https://github.com/blago-white/leftover-refresher/assets/94391766/03505925-8cf4-4ce2-9d80-213566150d32" alt="reflogo"/>
</p>

# Leftover Refresher
__This is a script for synchronizing product balances on different platforms, saving hundreds of hours spent on synchronizing data between platforms__

## The Model 🚀
This application is built around a master-slave model\
The data on the slave supplier is updated according to the data of the lead supplier

## Realization Advantages ⭐
1. Modularity\
  <sub>Use DI Pattern. The cost of changes is minimal</sub>
2. Asynchrony\
  <sub>Made on aiohttp with asyncio, very fast</sub>
3. Lightweight\
  <sub>Without db and fremeworks</sub>
4. Simplicity\
  <sub>A couple of lines on the command line and the service works for you</sub>

## Start Work ✅
1. Clone this repository
2. Create python 3.11 venv in dir with project
3. Activate venv
4. Install depencies\
  <sub>pip install -r requirements.txt</sub>
6. Go to the dir <code>/src/</code>
7. Fill the config.ini file in <code>/src/config/config.ini</code>
8. Update the settings in <code>/src/config/settings.py</code>
9. Run the command: <code>python main.py</code>

### Congratulations! 🎉
