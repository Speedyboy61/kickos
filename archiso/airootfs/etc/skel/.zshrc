if [[ -o interactive ]] && [[ "$TERM" != "dumb" ]] && [[ -z "$FASTFETCH_RAN" ]]; then
    export FASTFETCH_RAN=1
    fastfetch
fi
