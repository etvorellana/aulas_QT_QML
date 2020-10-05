// anima_01.qml

import QtQuick 2.5

Image {
    id: root
    source: "Imagens/background.png"

    property int padding: 40
    property int duration: 4000
    property bool running: false
    property bool forward: false

    Image {
        id: box
        x: root.padding;
        y: (root.height-height)/2
        source: "Imagens/box_green.png"

        NumberAnimation on x {
            to: root.width - box.width - root.padding
            duration: root.duration
            running: root.running
        }

        NumberAnimation on x {
            to: root.padding
            duration: root.duration
            running: root.forward
        }

        RotationAnimation on rotation {
            to: 360
            duration: root.duration
            running: root.running
        }

        RotationAnimation on rotation {
            to: 0
            duration: root.duration
            running: root.forward
        }
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            if (root.running == false & root.forward == false){
                root.running = true
            }else{
                if (root.running){
                    root.running = false
                    root.forward = true
                }else{
                    root.running = true
                    root.forward = false
                }
            }
        }
    }
}