// TLineEditV1.qml

import QtQuick 2.5 

Rectangle {
    width: 96; height: input.height + 12
    color: "lightsteelblue"
    border.color: "gray"
    
    property alias text: input.text
    property alias input: input

    TextInput {
        id: input
        anchors.fill: parent
        anchors.margins: 4
        focus: true
    }
}