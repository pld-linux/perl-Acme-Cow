. /etc/sysconfig/cowsay
if [ ! -n "$TEXT" ]; then
	TEXT="I Love GNU"
fi

if [ -n "$EYES" ]; then
	EYES="-e $EYES"
fi

if [ -n "$COW" ]; then
	COW="-f $COW"
fi
cow$TYPE $EYES $COW $TEXT
echo
