// LoginApp_00.qml

import QtQuick 2.5
import QtQuick.Window 2.5
import QtQuick.Controls 2.5

import MyTools 1.0

Window {
    // Definir a Janela Principal 
    id: root  // o id
    visible: true 
    property bool identOk: false
    width: 250; height: 400 // o tamanho
    /* Defines the window's maximum size. 
        This is a hint to the window manager to prevent 
        resizing above the specified width and height.*/
    maximumWidth: 250; maximumHeight: 400 
    minimumWidth: 250; minimumHeight: 400
    
    title: qsTr("Crachá") // o título da Janela

    Funcionario{
        id: funcionario
    }
    // Item {
    //     width: 20    
    //     height: 20
    //     anchors.bottom: parent.bottom
    //     QRCImage{
    //         id:qrcImage
    //         anchors.fill: parent
    //     }

    // }

    Image {
        id: bck_img
        anchors.fill: parent
        fillMode: Image.Stretch
        opacity: 0.5
        source: "Imagens/modelo.png"

        Image {
            id: imgLogo
            anchors.left: parent.left
            anchors.leftMargin : 30
            anchors.top: parent.top
            anchors.topMargin : 90
            width: parent.width/3
            fillMode: Image.PreserveAspectFit 
            source: funcionario.logo
            visible: root.identOk 
        }

        Image {
            id: imgFuncionario
            anchors.right: parent.right
            anchors.rightMargin : 30
            anchors.top: parent.top
            anchors.topMargin : 90
            width: parent.width/3
            fillMode: Image.PreserveAspectFit 
            source: funcionario.imgFuncionario
            visible: root.identOk 
        }

        Label {
            id: nomeEmpresa
            anchors.left: parent.left
            anchors.leftMargin : 30
            anchors.top: imgLogo.bottom
            anchors.topMargin: 5
            width: imgLogo.width
            background: Rectangle{
                anchors.fill: parent
                opacity: 1
                color: "#ffffff"
                radius:2
            }
            horizontalAlignment: Text.AlignHCenter
            text: funcionario.nomeEmpresa
            font.bold: true
            wrapMode: Text.WordWrap
            visible: root.identOk
        }

        Label {
            id: nomeFuncionario
            anchors.right: parent.right
            anchors.rightMargin : 30
            anchors.top: imgFuncionario.bottom
            anchors.topMargin: 50
            width: bck_img.width - 80
            background: Rectangle{
                anchors.fill: parent
                opacity: 1
                color: "#ffffff"
                radius:2
            }
            horizontalAlignment: Text.AlignHCenter
            text: funcionario.nomeFuncionario
            font.bold: true
            visible: root.identOk
        }
    }

    Button{
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        text: "Identifique-se"
        onClicked:{  //Aqui conectamos a um slot de autenticação
            root.identOk = true
            visible = false
            bck_img.opacity = 1.0
            //qrcImage.data = funcionario.nomeFuncionario + "\n" + funcionario.nomeEmpresa
        }
    }

    
    //Image {

        //usrImg = "Imagens/pessoa.png"

    //}
}