import { useState, useEffect } from 'react'
import RecordRTC, { invokeSaveAsDialog, StereoAudioRecorder } from 'recordrtc';
import styles from '../../styles/Home.module.css'
export default function Recorder({ username, method }) {
    const [audioBlob, setAudioBlob] = useState()
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
            .then(res => { setButtonText(res) 
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
            const sleep = m => new Promise(r => setTimeout(r, m));
            await sleep(5000);
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
        <button onClick={handleRecordClick} style={{ backgroundColor: buttonColor }}>{buttonText}</button>
    </div>)
}
