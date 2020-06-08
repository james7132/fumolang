# fumolang

Fumolang is a low-level, compiled, non-portable, esoteric programming langauge
based on the popular
[FumoFumo Touhou plush series](https://en-dic.pixiv.net/a/FumoFumo)
by [Gift](https://www.gift-gift.jp).

## Language Spec

Fumolang directly compiles to binary and only has two keywords that directly
translate into one bit in the compiled output:

 * `Fumo` - 0
 * `FumoFumo` - 1

The language is case-insensitive, and any variation of these two keywords is
accepted. Each word must be seperated by whitespace, and any other non-whitespace
token will be treated as comments.

This means source code is not portable and must be rewritten for every target
platform

## Examples

A example source code for linux-amd64 can be found in the `examples/`
directory.

## Compilation

```
TODO(james7132): Document
```

## Decompilation

```
TODO(james7132): Document
```

## FAQ

### Why do this?

Fumos.

### Compiling the decompilation output results in different results, that's a bug!

Who cares? Fumo.
