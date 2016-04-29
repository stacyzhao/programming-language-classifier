import glob


def read_files():
    folders = ["binarytrees", "binarytreesredux", "chameneousredux", "redux",
               "fasta", "fastaredux", "Include", "knucleotide", "mandelbrot",
               "meteor", "nbody", "regexdna", "revcomp", "spectralnorm",
               "threadring", "pidigits"]
            #    "pidigits"
    extensions = ["gcc",  "c", "csharp", "sbcl", "clojure",
                  "hack", "java", "javascript", "ocaml", "perl",
                  "php", "py", "jruby", "yarv", "scala", "racket", "ghc"]

    texts = []

    for folder in folders:
        path = "benchmarksgame/bench/" + folder + "/*."

        for x in extensions:
            files = glob.glob(path + x)

            for file in files:
                with open(file, encoding="ISO-8859-1") as f:
                    texts.append(f.read())
    return texts

print(len(read_files()))
