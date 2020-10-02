// LoginApp_00.qml

import QtQuick 2.5
import QtQuick.Window 2.5

Window {
    // Definir a Janela Principal 
    id: root  // o id
    visible: true 
    width: 200; height: 150 // o tamanho
    title: qsTr("Login") // o título da Janela

    // O container da Janela
    Rectangle {
        anchors.fill: parent

        Text {
        
            id: msg_lbl
            text: "Não aperte o botão!!!"
            x: 30; y: 30 //localiza o label na tela
 
        }
        Rectangle {

            id: sair_btn
            x: 50; y: 70
            width: btn_lbl.width + 8
            height: btn_lbl.height + 8
            color: "lightsteelblue"
            border.color: "slategrey"
            radius: 8

            Text {
                id: btn_lbl
                anchors.centerIn: parent
                text: 'Aperte aqui!'
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    root.close()
                }
            }
        }
    }
}