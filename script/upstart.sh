#!/bin/sh

# --------------------------------------------------------------------------#
# Copyright (c) 20011 MadeiraCloud, All Rights Reserved						#
# --------------------------------------------------------------------------#

# user/group
groupadd madeiracloud 2>/dev/null
useradd -mr -g madeiracloud madeiracloud 2>/dev/null
chown -R madeiracloud:madeiracloud /usr/share/madeiracloud

cat <<ENDINIT > /etc/init.d/madeiracloud
#!/bin/sh

# --------------------------------------------------------------------------#
# Copyright (c) 20011 MadeiraCloud, All Rights Reserved						#
# --------------------------------------------------------------------------#

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0

BIN="/usr/bin/madeiracloud.py"
PROG="MadeiraCloud"
LOCK="/var/lock/subsys/madeiracloud"
RETVAL=0

user=${USER-ajaxterm}
RETVAL=0

start() {
    echo -n $"Starting $PROG: "
    $BIN
    RETVAL=$?
    echo
    [ $RETVAL = 0 ] && touch ${lockfile}
    return $RETVAL
}

stop() {
    echo -n $"Stopping $prog: "
    killproc $PROG
    RETVAL=$?
    echo
    [ $RETVAL = 0 ] && rm -f $LOCK
}

# See how we were called.
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
        status $prog
        RETVAL=$?
        ;;
    restart)
        stop
        start
        ;;
    *)
    echo $"Usage: $prog {start|stop|status|restart}"
    exit 1
esac

exit $RETVAL

ENDINIT

chmod 755 /etc/init.d/madeiracloud

rm -f /etc/rc*.d/*madeiracloud
ln -s "/etc/init.d/madeiracloud" "/etc/rc1.d/K50madeiracloud"
ln -s "/etc/init.d/madeiracloud" "/etc/rc2.d/S50madeiracloud"
ln -s "/etc/init.d/madeiracloud" "/etc/rc3.d/S50madeiracloud"
ln -s "/etc/init.d/madeiracloud" "/etc/rc4.d/S50madeiracloud"
ln -s "/etc/init.d/madeiracloud" "/etc/rc5.d/S50madeiracloud"
ln -s "/etc/init.d/madeiracloud" "/etc/rc6.d/K50madeiracloud"
