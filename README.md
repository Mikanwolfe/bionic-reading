# Bionic Text Converter

Usage:

```
py bionic-reading.py [input file] [output file]
```

e.g.

```
py bionic-reading.py in.txt out.md
```

You can use an online markdown editor such as [Dillinger](https://dillinger.io/) or a standalone one such as [Typora](https://typora.io/) to see the formatted output.

Check it out for yourself:

----

## Regular Text

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint  occaecat cupidatat non proident, sunt in culpa qui officia deserunt  mollit anim id est laborum.

----

## Converted

**Lo**rem **ip**sum **do**lor **si**t **am**et, **consec**tetur **adipi**scing **el**it, **se**d **d**o **eius**mod **tem**por **incid**idunt **u**t **lab**ore **e**t **dol**ore **ma**gna **aliq**ua. **U**t **en**im **a**d **mi**nim **veni**am, **qu**is **nost**rud **exerci**tation **ulla**mco **labo**ris **ni**si **u**t **aliq**uip **e**x **e**a **comm**odo **conse**quat. **Du**is **au**te **ir**ure **do**lor **i**n **repreh**enderit **i**n **volu**ptate **ve**lit **es**se **cil**lum **dol**ore **e**u **fug**iat **nu**lla **pari**atur. **Exce**pteur **si**nt **occa**ecat **cupi**datat **no**n **proi**dent, **su**nt **i**n **cu**lpa **qu**i **offi**cia **dese**runt **mol**lit **an**im **i**d **es**t **labo**rum.

----

Bionic reading was trending a few days ago on Reddit, the idea is that you emphasise the first few letters of a word to make speed-reading easier. To test this on your own documents, this short python script converts plaintext input into formatted markdown outputs.

For more information, check out their website. https://bionic-reading.com/