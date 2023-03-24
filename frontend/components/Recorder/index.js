import { useState, useEffect } from 'react'
import RecordRTC, { invokeSaveAsDialog, StereoAudioRecorder } from 'recordrtc';
import styles from '../../styles/Home.module.css'
export default function Recorder({ username, method }) {
    const [audioBlob, setAudioBlob] = useState()
    const [pBar,showPBar]=useState(false)
    const [pWidth,setPWidth]=useState(100)
    useEffect(() => {
        if (audioBlob) {
            var data = new FormData()
            data.append('file', audioBlob, 'file')
            data.append('username', username)
            fetch(`http://localhost:5000/${method}`, {
                method: "POST",
                body: data
            })
            .then(response => response.json())
            .then(res => { 
                showPBar(false)
                setButtonText(res) 
                if(res==='SUCCESS') setButtonColor('greenyellow')
             else setButtonColor('red')})
            .catch(err => console.log(err));

        }
    }, [audioBlob])
    function handleRecordClick() {
        navigator.mediaDevices.getUserMedia({
            audio: true
        }).then(async function (stream) {
            let recorder = RecordRTC(stream, {
                type: 'audio',
                recorderType: StereoAudioRecorder,
                mimeType: 'audio/wav',
            });
            recorder.startRecording();
            showPBar(true)
            const sleep = m => new Promise(r => setTimeout(r, m));
            const i=setInterval(()=>{
                setPWidth(s=>{
                    return s-1
                })
            },45)
            await sleep(5000);
            clearInterval(i)
            
            recorder.stopRecording(function () {
                let blob = recorder.getBlob();
                setAudioBlob(blob)
            });
        });
        if (buttonText === 'RECORD') {
            setButtonColor('cyan')
            setButtonText('RECORDING')
        }
        else {
            setButtonColor('orange')
            setButtonText('RECORD')
        }
    }
    const [buttonText, setButtonText] = useState('RECORD')
    const [buttonColor, setButtonColor] = useState('orange')
    return (<div className={styles.voicesection}>
        {pBar && <div className={styles.progressbar} style={{ width:`${pWidth}%`}}></div>}
        <button onClick={handleRecordClick} style={{ backgroundColor: buttonColor }}>{buttonText}</button>
    </div>)
}
