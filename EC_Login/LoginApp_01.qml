// LoginApp_01.qml

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
        Button {
            id: sair_btn
            x: 50; y: 70
            text: 'Aperte aqui!'
            onClicked: {
                root.close()
            }
        }
    }
}