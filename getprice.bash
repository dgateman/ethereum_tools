sed 's/\$//g' etherawktemp > etherawktemp2 ; sed 's/\%//g' etherawktemp2 > etherawktemp3; sed 's/.*=//' etherawktemp3 | sed 's/.\{4\}$//' | awk '{$2=$2}1'
