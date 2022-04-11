# normalize-audio

Normalize wav files in `--src` directory, include recursive contents.

Processed wav files are saved to `--dest` directory with inner directory structure preserved. 

Conversion:
- 44.1k sample rate
- 16 bit depth
- gain normalized to -0.1 of peak

## Installation

Requires [SoX](http://sox.sourceforge.net/), "the Swiss Army knife of sound processing programs".

```
git clone https://github.com/eddiechapman/normalize-audio.git
cd normalize-audio
python3 -m venv venv
source venv/bin/activate
pip install .
```

## Usage

```
normalize --src ~/Music/samples/ --dest ~/Music/samples_converted/
```



