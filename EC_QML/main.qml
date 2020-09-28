import QtQuick 2.5 
 
Image {
    id: root
    source: "Imagens/background.png"

    Image {
        id: pole
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        source: "Imagens/pole.png"
    }

    Image {
        id: wheel
        anchors.centerIn: parent
        source: "Imagens/pinwheel.png"
        Behavior on rotation {
            NumberAnimation {
                duration: 250
            }
        }
    }

    MouseArea {
        anchors.fill: parent
        onClicked: wheel.rotation += 90
    }


}