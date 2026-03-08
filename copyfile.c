#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
        return 1;
    }
    FILE *src = fopen(argv[1], "rb");
    if (src == NULL)
    {
        perror("Error opening source file");
        return 1;
    }
    FILE *dst = fopen(argv[2], "wb");
    if (dst == NULL)
    {
        perror("Error opening destination file");
        fclose(src);
        return 1;
    }
    char buffer[4096];
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, sizeof(buffer), src)) > 0)
    {
        size_t bytes_written = fwrite(buffer, 1, bytes_read, dst);
        if (bytes_written != bytes_read)
        {
            perror("Error writing to destination file");
            fclose(src);
            fclose(dst);
            return 1;
        }
    }
    if (ferror(src))
    {
        perror("Error reading source file");
        fclose(src);
        fclose(dst);
        return 1;
    }
    printf("Copied '%s' -> '%s'\n", argv[1], argv[2]);
    fclose(src);
    fclose(dst);
    return 0;
}
