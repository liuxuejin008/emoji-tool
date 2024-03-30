import replicate

input = {
    "prompt": "A TOK emoji of a man",
    "apply_watermark": False
}

output = replicate.run(
    "fofr/sdxl-emoji:dee76b5afde21b0f01ed7925f0665b7e879c50ee718c5f78a9d38e04d523cc5e",
    input=input
)
print(output)
