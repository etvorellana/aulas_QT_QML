// anima_02.qml

import QtQuick 2.5

Item {
    id: root
    width: background.width; height: background.height

    Image {
        id: background
        source: "Imagens/background_medium.png"
    }

    MouseArea {
        anchors.fill: parent
        onClicked: {
            greenBox.y = blueBox.y = redBox.y = root.height - greenBox.height
        }
    }

    ClickableImageV2 {
        id: greenBox
        x: 40; y: root.height-height
        source: "Imagens/box_green.png"
        text: "animation on property"
        NumberAnimation on y {
            to: 40; duration: 4000
        }
    }

    ClickableImageV2 {
        id: blueBox
        x: (root.width-width)/2; y: root.height - greenBox.height
        source: "Imagens/box_blue.png"
        text: "behavior on property"
        Behavior on y {
            NumberAnimation { duration: 4000 }
        }

        onClicked: y = 100
        // random y on each click
        // onClicked: y = 40+Math.random()*(205-40)
    }

    ClickableImageV2 {
        id: redBox
        x: root.width-width-40; y: root.height - greenBox.height
        source: "Imagens/box_red.png"
        onClicked: anim.start()
        //onClicked: anim.restart()

        text: "standalone animation"

        NumberAnimation {
            id: anim
            target: redBox
            properties: "y"
            to: 40
            duration: 4000
        }
    }
}
