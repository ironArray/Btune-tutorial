# Btune-tutorial

First, clone this repo with:

    git clone https://github.com/Blosc/Btune-tutorial

Then, make sure that you are using a Python environment with Python 3.10 or 3.11.  For example, if you are using conda, you can do that easily with:

    conda create -n btune-tutorial python=3.11
    conda activate btune-tutorial


Install the Btune plugin:

    pip install blosc2-btune -U

# Genetic tuning

To use Btune with Blosc2, set the `BTUNE_TRADEOFF` environment variable to a floating-point number between 0 (to optimize speed) and 1 (to optimize compression ratio). Additionally, you can use `BTUNE_PERF_MODE` to optimize compression, decompression, or to achieve a balance between the two by setting it to `COMP`, `DECOMP`, or `BALANCED`, respectively.

For a trace of what is going on, set the `BTUNE_TRACE` environment variable.  With that, go to the `inference/` directory and type:

```
BTUNE_TRACE=1 BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=COMP python rand_int.py
```

```
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
TRACE: Environment variable BTUNE_MODELS_DIR is not defined
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 11, Repeat Mode - STOP
TRACE: Environment variable BTUNE_MODELS_DIR is not defined
WARNING: Empty metadata, no inference performed
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |      0 |     1 |       8 |         0 |           8 |         4 |         4 |  0.000105 |      1.97x |    CODEC_FILTER |    HARD | W
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |      0 |     0 |       8 |         0 |           8 |         4 |         4 |   6.9e-05 |      2.07x |    CODEC_FILTER |    HARD | W
|        lz4 |      1 |     1 |       8 |         0 |           8 |         4 |         4 |  2.43e-05 |      3.97x |    CODEC_FILTER |    HARD | W
|        lz4 |      1 |     0 |       8 |         0 |           8 |         4 |         4 |  1.88e-05 |      3.91x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     1 |       8 |         0 |           8 |         4 |         4 |  2.91e-05 |      4.52x |    CODEC_FILTER |    HARD | W
|        lz4 |      2 |     0 |       8 |         0 |           8 |         4 |         4 |  2.42e-05 |      4.46x |    CODEC_FILTER |    HARD | -
|    blosclz |      0 |     1 |       8 |         0 |           8 |         4 |         4 |  8.66e-05 |      1.98x |    CODEC_FILTER |    HARD | -
|    blosclz |      0 |     0 |       8 |         0 |           8 |         4 |         4 |  6.17e-05 |      2.08x |    CODEC_FILTER |    HARD | -
|    blosclz |      1 |     1 |       8 |         0 |           8 |         4 |         4 |  3.43e-05 |      3.97x |    CODEC_FILTER |    HARD | -
|    blosclz |      1 |     0 |       8 |         0 |           8 |         4 |         4 |  4.68e-05 |      3.82x |    CODEC_FILTER |    HARD | -
|    blosclz |      2 |     1 |       8 |         0 |           8 |         4 |         4 |   4.4e-05 |      4.47x |    CODEC_FILTER |    HARD | -
|    blosclz |      2 |     0 |       8 |         0 |           8 |         4 |         4 |  4.98e-05 |      4.35x |    CODEC_FILTER |    HARD | -
|        lz4 |      2 |     1 |       8 |         0 |           8 |         4 |         4 |  2.46e-05 |      4.52x |    THREADS_COMP |    HARD | W
|        lz4 |      2 |     1 |       7 |         0 |           8 |         4 |         4 |  2.44e-05 |      4.52x |          CLEVEL |    HARD | -
|        lz4 |      2 |     1 |       9 |         0 |           8 |         4 |         4 |  2.47e-05 |      4.52x |          CLEVEL |    HARD | W
|        lz4 |      2 |     1 |       8 |         0 |           8 |         4 |         4 |  2.45e-05 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         0 |           8 |         4 |         4 |  2.45e-05 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       8 |         0 |           8 |         4 |         4 |  2.47e-05 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       9 |         0 |           8 |         4 |         4 |  2.47e-05 |      4.52x |          CLEVEL |    SOFT | -
|        lz4 |      2 |     1 |       8 |         0 |           8 |         4 |         4 |  2.43e-05 |      4.52x |          CLEVEL |    SOFT | -
NDArray 'rand_int_inference.b2nd' created!
```

You can see in the column `Winner` whether the combination is a winner (`W`), it does not improve the previous winner (`-`) or it is a special value chunk meaning that it is really easy to compress no matter the compression parameters (`S`); in the latter case Btune cannot determine whether this is a winner or not.

Cool! We have done our first attempt at guessing the best parameters.

## Exercise 1

Execute the previous command changing the different parameters (passed as environment variables).  Some examples:

- BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=0.1 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=0.1 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=0.9 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=0.9 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=1.0 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=1.0 BTUNE_PERF_MODE=DECOMP
- BTUNE_TRADEOFF=.0 BTUNE_PERF_MODE=COMP
- BTUNE_TRADEOFF=.0 BTUNE_PERF_MODE=DECOMP

Look at the score and the compression ratios columns.  The smaller the score, the less time it takes to compress/decompress (the faster it is).  Compression ratios are expressed as [uncompressed size / compressed size](https://en.wikipedia.org/wiki/Data_compression_ratio), i.e. the larger, the more storage is saved.

### Questions

+ Which are the codecs and filters that win for tradeoffs favoring compression speed?  Which are the winners for compression ratio?
+ What's the perceived difference when `BTUNE_PERF_MODE` is set to 'COMP' and 'DECOMP' respectively?
+ What happens at extreme values of `BTUNE_TRADEOFF` (0 and 1)?

# Training Btune and creating a NN model

Besides genetic tuning, Btune can also use neural network models that are trained for specific datasets.  With that, Btune can take better informed decisions on the codecs/filters that can lead to the best tradeoff between speed and compression ratio.

For training a model, you need to install the btune-training package.  First download all the wheels for it by visiting https://digistorage.net/scgpku0k, and unzip it if needed:

```shell
unzip btune-training-wheels.zip
```

Then install the one that correspond to your platform; for example, if you are on a Mac with an ARM64 processor:

```shell
python -m pip install btune-training-wheels/btune_training-1.0.0-cp310-cp310-macosx_11_0_arm64.whl -U
```

and finally, install the dependencies (in the root directory of this tutorial repo):

```shell
cd <root_tutorial_repo>
python -m pip install -r requirements-training.txt -U
```

Then, let's create a file that follows the same distribution as the one in the previous section. This time, we will be adding a `-t` flag, meaning that we are going to create a larger file (the training process requires relatively large datasets for being accurate enough) :

```shell
cd inference
python rand_int.py -t
ls -l rand_int_training.b2nd
```

Now, we can start the training process.  Let's first do the necessary measurements (for entropy and cratios and times for codecs/filters):

```shell
cd ../training
python gather_data.py ../inference/rand_int_training.b2nd
```

We can proceed with the training as such.  Let's start generating models for 'c'ompression:

```shell
python training_chunk.py c ../inference rand_int_training.b2nd.meas
```

In the output we can see the most predicted codecs and filters for every tradeoff.  For example, on my machine I get:

```
                  1st most predicted               2nd most predicted 3rd most predicted Mean cratio Mean cspeed (GB/s) Mean dspeed (GB/s)
0.0  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.91               2.55               2.57
0.1  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.91               2.55               2.57
0.2  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.91               2.55               2.57
0.3  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.91               2.55               2.57
0.4  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.91               2.55               2.57
0.5  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.91               2.55               2.57
0.6         lz4-bitshuffle-nosplit-5  lz4-shuffle-bytedelta-nosplit-5                  -        4.46               2.11               2.25
0.7         lz4-bitshuffle-nosplit-5                                -                  -        4.46               2.11               2.25
0.8         lz4-bitshuffle-nosplit-5                                -                  -        4.46               2.11               2.25
0.9         lz4-bitshuffle-nosplit-5                                -                  -        4.46               2.11               2.25
1.0        zstd-bitshuffle-nosplit-9                                -                  -        4.55               0.07               2.38
```

Now, let's generate the models for 'd'ecompression:

```shell
python training_chunk.py d ../inference rand_int_training.b2nd.meas
```

Here we have the most predicted codecs and filters:

```
                      1st most predicted            2nd most predicted 3rd most predicted Mean cratio Mean cspeed (GB/s) Mean dspeed (GB/s)
0.0  blosclz-shuffle-bytedelta-nosplit-5                             -                  -        3.82               0.89                3.9
0.1  blosclz-shuffle-bytedelta-nosplit-5                             -                  -        3.82               0.89                3.9
0.2  blosclz-shuffle-bytedelta-nosplit-5                             -                  -        3.82               0.89                3.9
0.3  blosclz-shuffle-bytedelta-nosplit-5                             -                  -        3.82               0.89                3.9
0.4  blosclz-shuffle-bytedelta-nosplit-5                             -                  -        3.82               0.89                3.9
0.5  blosclz-shuffle-bytedelta-nosplit-5  blosclz-bitshuffle-nosplit-5                  -        3.82               0.89                3.9
0.6         blosclz-bitshuffle-nosplit-5                             -                  -        4.35               0.89               3.29
0.7         blosclz-bitshuffle-nosplit-5                             -                  -        4.35               0.89               3.29
0.8            zstd-bitshuffle-nosplit-6                             -                  -        4.54               0.51               2.57
0.9            zstd-bitshuffle-nosplit-6                             -                  -        4.54               0.51               2.57
1.0            zstd-bitshuffle-nosplit-9                             -                  -        4.55               0.07               2.38
```

Now we have our models ready to be used:

```shell
ls model*
```

```output
model_comp.json      model_comp.tflite    model_decomp.json    model_decomp.tflite
```

Note how we have two set of files that store the models: two files for the 'comp'ression model and another two for the "decomp"ression one.  These will be used to predict (infer) the codecs and filters for new datasets.  Note that these models are mainly useful for datasets that follows the same patterns as those used for the training.

Let's move them to another directory:

```shell
mkdir ../inference/rand_int_training.model
mv model* ../inference/rand_int_training.model
```

# Using trained Btune models

With the models, we can predict the best codecs/filters during the creation of new datasets.

## Inference (predictions) in COMPression mode

Let's do the inference for COMPression performance mode:

```shell
cd ../inference
BTUNE_TRADEOFF=0.5 BTUNE_USE_INFERENCE=-1 BTUNE_PERF_MODE=COMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=rand_int_training.model python rand_int.py
```

and the output is something like:

```
Creating data for inference purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
TRACE: time load model: 0.013766
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 11, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
TRACE: time load model: 0.000186
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000327 inference=0.000830
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   0.00038 |      3.97x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000142 inference=0.000006
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.36e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000143 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   1.3e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000140 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.33e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000137 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.34e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000204 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  4.58e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000154 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.34e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000111 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.42e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000115 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.37e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000109 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.42e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000117 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.47e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000136 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  2.48e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000112 inference=0.000008
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.61e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000105 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.43e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000106 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.38e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000102 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.35e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000102 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.38e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000104 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.39e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000105 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.36e-05 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000101 inference=0.000005
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  1.37e-05 |      3.97x |    CODEC_FILTER |    HARD | -
NDArray 'rand_int_inference.b2nd' created!
```

### Exercise 2: experiment with different parameters in COMP performance mode

In particular, you can try with different tradeoffs:

- BTUNE_TRADEOFF=0.0  # best speed; compression ratio does not matter
- BTUNE_TRADEOFF=0.3  # good speed, but add some weight to cratio
- BTUNE_TRADEOFF=0.5  # a balance between speed and cratio
- BTUNE_TRADEOFF=0.8  # good cratio, but speed is somewhat important too
- BTUNE_TRADEOFF=1.0  # best compression ratio; speed does not matter

Also, you can set `BTUNE_USE_INFERENCE` to a positive value to use inference only for the first iterations; after that, Btune will fall back into a 'gentle' genetic mode, also called 'tweaking', for fine-tuning some params like `clevel` or `splitmode`.  Note that the tweaking will start from the set of compression parameters that have won in the previous

### Exercise3: combine inference and tweaking modes

Try with the next values:

- BTUNE_USE_INFERENCE=3   # only do inference for the first 3 chunks and then use tweaking
- BTUNE_USE_INFERENCE=10  # only do inference for the first 10 chunks and then use tweaking

* How the parameters are tested now?  Can you see the new pattern?
* How predictions differ from complete inference?

## Inference (predictions) in DECOMPression performance mode

Let's use the model in DECOMPression performance mode now:

```shell
BTUNE_TRADEOFF=0.5 BTUNE_USE_INFERENCE=-1 BTUNE_PERF_MODE=DECOMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=rand_int_training.model python rand_int.py
```

```
Creating data for inference purposes...
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: DECOMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 10, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
TRACE: time load model: 0.000626
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: DECOMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 11, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
TRACE: time load model: 0.000159
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000386 inference=0.000073
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000146 |      4.47x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000380 inference=0.000009
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  2.93e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000213 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000175 inference=0.000026
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.35e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000354 inference=0.000009
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.52e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000110 inference=0.000008
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.43e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=3 codec=0 filter=35 clevel=5 splitmode=2 time entropy=0.000263 inference=0.000007
|    blosclz |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  6.39e-06 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=3 codec=0 filter=35 clevel=5 splitmode=2 time entropy=0.000104 inference=0.000006
|    blosclz |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  6.11e-06 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000131 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.35e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000233 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.29e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000107 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.33e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000104 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.25e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000101 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.24e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000102 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000183 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |   1.3e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=3 codec=0 filter=35 clevel=5 splitmode=2 time entropy=0.000105 inference=0.000005
|    blosclz |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  5.83e-06 |      3.97x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000109 inference=0.000006
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.32e-05 |      4.47x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000106 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000108 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.26e-05 |      4.47x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=2 codec=0 filter=2 clevel=5 splitmode=2 time entropy=0.000101 inference=0.000005
|    blosclz |      2 |     1 |       5 |         0 |           8 |         6 |         6 |  1.27e-05 |      4.47x |    CODEC_FILTER |    HARD | -
NDArray 'rand_int_inference.b2nd' created!
```

### Exercise 4: experiment with different parameters in DECOMP performance mode

Go to instructions in exercises 2 and 3 and retry them for DECOMP mode.

## Final exercise: train models with your own datasets!

Go copy the `rand_int.py` script to some other name (e.g. `my_data.py`) and use some other dataset than the one there (you can read them from your favorite format, like HDF5 or Zarr).  Change the name of the output file too (but keep the .b2nd extension, as it will remain a Blosc2 format).  Train with that one, and store the model in another directory.

Indeed, you can bring your own data, create a NumPy array out of it, and export it to the Blosc2 format.  We recommend to make sure to populate the new array with at least 3000 chunks; in our experience, this is a good minimum to ensure a decent training.

Play with the parameters stated in exercises 2 and 3 and get your own conclusions.  Raise your hand and let's have a discussion in case you get 'interesting' results.

That's all folks; hope you have enjoyed the ride!  For more information about Btune, check out: https://ironarray.io/btune

Inquiries?  contact@ironarray.io
