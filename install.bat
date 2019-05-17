git clone https://github.com/charliewolf/pynder.git
cd pynder
git fetch origin +refs/pull/211/merge
git checkout -qf FETCH_HEAD
python -m pip install --force-reinstall --no-deps .
python -m pip install -r .\requirements.txt
