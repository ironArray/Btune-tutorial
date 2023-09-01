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

Cool! We have done our first attempt at guessing the best parameters...
