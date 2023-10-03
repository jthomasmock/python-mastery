library(dplyr)
library(stringr)
library(fs)

all_files <- fs::dir_ls("Exercises/")

all_ex <- str_subset(all_files, "ex[0-9]")  |> 
    str_subset(".md")

read_add_quarto <- function(file){
    
    all_lines <- read_lines(file)

    title <- str_subset(all_lines, "# Exercise") |> 
        str_remove(pattern ="# ")

    base_text <- c(
        "---",
        "format: html",
        "jupyter: python3",
        "---"
    )

    all_lines <- str_replace_all(all_lines, "```python", "```{python}")
    
    out_text <- c(base_text, all_lines)

    file_root <- file |> 
        fs::path_file() |> 
        fs::path_ext_remove()

    file_out <- glue::glue("Quarto/{file_root}.qmd")

    out_text |> 
        write_lines(file_out)
}

# test it
read_add_quarto(all_ex[1])

# do it
map(all_ex, read_add_quarto)


