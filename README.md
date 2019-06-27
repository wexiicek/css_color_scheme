# scss_color_scheme
Nobody likes hard coded colors, right? This repo is here for you.

## What does it do?
This tool looks for hardcoded colors inside `.scss` files and creates a color scheme. It will also accept some other formats (*.less*, *.sass*), but the functionality is not supported yet.

## Prerequisities
You need to have a local installation of Python. And you have to be able to open *Terminal* or *cmd*.

## Usage
`python scss_color_scheme <path_to_scheme_file> [-r]`
#### At the moment this tool only works in the directory where it is located.
You can choose an existing file (will be **rewritten**!) or non-existing file (will be created).
`-r` Recursively search inside folders too! (This feature will currently only look into the next level folders!).
