#!/bin/bash

$OPENSHIFT_GO_DIR/bin/control stop

export GOPATH=$GOPATH:$OPENSHIFT_PGSAMPAPP_DIR/golang/gocode-raw
export logf=$OPENSHIFT_PGSAMPAPP_DIR/golang.log
cd $OPENSHIFT_PGSAMPAPP_DIR/golang
go build $OPENSHIFT_PGSAMPAPP_DIR/golang/WebApp.go 2>&1 > $logf
nohup $OPENSHIFT_PGSAMPAPP_DIR/golang/WebApp 2>&1 > $logf &
ret=$?
npid=$!
if [ $ret -eq 0 ]; then
        echo "$npid" > "$OPENSHIFT_PGSAMPAPP_DIR/go.pid"
else
        echo "go Application failed to start - $ret"
        exit $ret
fi

