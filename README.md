# Btune-tutorial

First, clone this repo with:

    $ git clone https://github.com/Blosc/Btune-tutorial

And install the Btune plugin:

    $ pip install blosc2-btune

# Genetic tuning

To use Btune with Blosc2, set the `BTUNE_TRADEOFF` environment variable to a floating-point number between 0 (to optimize speed) and 1 (to optimize compression ratio). Additionally, you can use `BTUNE_PERF_MODE` to optimize compression, decompression, or to achieve a balance between the two by setting it to `COMP`, `DECOMP`, or `BALANCED`, respectively.

For a trace of what is going on, set the `BTUNE_TRACE` environment variable.  With that, go to the `inference/` directory and type:

```
$ BTUNE_TRACE=1 BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=COMP python rand_int.py
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

For training a model, you need to install the btune-training package.  First download all the wheels for it by visiting https://digistorage.net/scgpku0k, and then:

```shell
unzip btune-training-wheels.zip
```

and then install the one that fits your package; for example:

```shell
python -m pip install btune-training-wheels/btune_training-1.0.0-cp310-cp310-macosx_11_0_arm64.whl
```

and finally the dependencies:

```shell
python -m pip install requirements-training.txt
```

Then, let's create a file that follows the same distribution as the one in the previous section:

```shell
cd inference
python rand_int.py -t
```

Now, we can start the training process.  Let's first do the necessary measurements (for entropy and cratios and times for codecs/filters):

```shell
cd ../training
python gather_data.py ...
```

We can proceed with the training as such.  Let's start generating models for 'c'ompression:

```shell
python training_chunk.py c ../inference rand_int_training.b2nd.meas
```

In the output we can see the most predicted codecs for every tradeoff.  For example:

```
                  1st most predicted               2nd most predicted 3rd most predicted Mean cratio Mean cspeed (GB/s) Mean dspeed (GB/s)
0.0  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.93               4.82                6.1
0.1  lz4-shuffle-bytedelta-nosplit-5                                -                  -        3.93               4.82                6.1
0.2  lz4-shuffle-bytedelta-nosplit-5         lz4-bitshuffle-nosplit-5                  -        3.93               4.82                6.1
0.3  lz4-shuffle-bytedelta-nosplit-5         lz4-bitshuffle-nosplit-5                  -        3.93               4.82                6.1
0.4  lz4-shuffle-bytedelta-nosplit-5         lz4-bitshuffle-nosplit-5                  -        3.93               4.82                6.1
0.5  lz4-shuffle-bytedelta-nosplit-5         lz4-bitshuffle-nosplit-5                  -        3.93               4.82                6.1
0.6  lz4-shuffle-bytedelta-nosplit-5         lz4-bitshuffle-nosplit-5                  -        3.93               4.82                6.1
0.7         lz4-bitshuffle-nosplit-5  lz4-shuffle-bytedelta-nosplit-5                  -        4.49                3.2               3.52
0.8         lz4-bitshuffle-nosplit-5                                -                  -        4.49                3.2               3.52
0.9         lz4-bitshuffle-nosplit-5        zlib-bitshuffle-nosplit-5                  -        4.49                3.2               3.52
1.0        zstd-bitshuffle-nosplit-9        zlib-bitshuffle-nosplit-5                  -        4.62               0.04               2.69
```

Now, let's generate the models for 'd'ecompression:

```shell
python training_chunk.py d ../inference rand_int_training.b2nd.meas
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

## Exercise 2: train your own dataset

Go to `rand_int.py` and use some dataset that is different form the one per default.  Train that one, and store the model in another directory.

Alternatively, take your data and export it to the Blosc2 format (and populate it with at least 3000 chunks).

# Using trained Btune models

With the models, we can predict the best codecs/filters during the creation of new datasets.  Let's do that now for COMPression performance mode:

```shell
cd ../inference
BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=COMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=rand_int_training.model BTUNE_USE_INFERENCE=-1 python rand_int.py
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
TRACE: time load model: 0.013347
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
Btune version: 1.0.1.dev
Performance Mode: COMP, Compression tradeoff: 0.500000, Bandwidth: 20 GB/s
Behaviour: Waits - 0, Softs - 5, Hards - 11, Repeat Mode - STOP
INFO: Model files found in the 'rand_int_training.model' directory
TRACE: time load model: 0.000214
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.001280 inference=0.000984
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000755 |         4x |    CODEC_FILTER |    HARD | W
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000199 inference=0.000007
|    Codec   | Filter | Split | C.Level | Blocksize | Shufflesize | C.Threads | D.Threads |   Score   |  C.Ratio   |   Btune State   | Readapt | Winner
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000115 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000369 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000266 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000219 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000115 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000220 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   9.8e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000221 inference=0.000009
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000135 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000193 inference=0.000009
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000132 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000199 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  8.02e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000395 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |     8e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000299 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   7.9e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000257 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000148 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000244 inference=0.000008
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  9.56e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000487 inference=0.000007
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000116 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000389 inference=0.000009
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000111 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000265 inference=0.000008
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  8.22e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000442 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000107 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000286 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |   9.4e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000223 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  8.12e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000206 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  7.07e-05 |         4x |    CODEC_FILTER |    HARD | -
TRACE: Inference category=7 codec=1 filter=35 clevel=5 splitmode=2 time entropy=0.000169 inference=0.000006
|        lz4 |     35 |     1 |       5 |         0 |           8 |         6 |         6 |  0.000111 |         4x |    CODEC_FILTER |    HARD | -
NDArray 'rand_int_inference.b2nd' created!
```

And when we want to use the model in DECOMPression performance mode:

```shell
BTUNE_TRADEOFF=0.5 BTUNE_PERF_MODE=DECOMP BTUNE_TRACE=1  BTUNE_MODELS_DIR=rand_int_training.model BTUNE_USE_INFERENCE=-1 python rand_int.py
```
