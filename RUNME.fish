
conda deactivate
echo 'Activating conda env : GlcJournal'
conda activate GlcJournal
echo 'Downloading journal.jl ...'
echo 'Updating download_history.txt ...'
python download.py
echo 'Exporting notebook to .py script ...'
jupyter nbconvert --to script Preprocessing.ipynb
python Preprocessing.py
conda deactivate

