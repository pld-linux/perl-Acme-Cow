. /etc/sysconfig/cowsay
if [ ! -n "$TEXT" ]; then
	TEXT="I Love GNU"
fi

if [ -n "$EYES" ]; then
	EYES="-e $EYES"
fi

if [ -n "$COW" ]; then
	if [ $COW = "random" ]; then
		COW="-r"
	else
		COW="-f $COW"
	fi
fi
cow$TYPE $EYES $COW $TEXT
echo
