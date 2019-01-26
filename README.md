# `ndshow`: A GUI tool for browsing NDS2 channels

`ndshow` is a modern replacement for the channel-name browsing functionality of
`dataviewer`, which is only available on-site (since it only recognizes NDS1).

## Using `nds_query` to search for channels at the command line

If you don't need or have access to the GUI function, you can always search for
channels using `nds_query`. In the example below, you can search for all
`H1:SYS-TIMING` channels that were available at LHO at the start of January 15,
2019:

```bash
nds_query \
    -n nds.ligo-wa.caltech.edu \
    -s `lalapps_tconvert Jan 15, 2019` \
    -d 1 \
    -l 'H1:SYS-TIMING*'
```

Get the prefixes to the LLO channels with:

```bash
sed -n '/^L/s/-/ /gp' llo-channels-post-er13.txt \
    | awk '{ print $1 }' \
    | sort \
    | uniq >llo-channels-post-er13-start.txt
```

Same for LHO:

```bash
sed -n '/^H/s/-/ /gp' lho-channels-post-er13.txt \
    | awk '{ print $1 }' \
    | sort \
    | uniq >lho-channels-post-er13-start.txt
```
