import styles from '../../styles/Home.module.css'
import Head from 'next/head'
import { useEffect, useRef, useState } from 'react'
import dynamic from 'next/dynamic';
const Recorder = dynamic(() => import('../../components/Recorder/index.js'), { ssr: false });

export default function Register() {
    function fetchuser(username) {
        var data = new FormData()
        data.append('username', username)
        return fetch('http://localhost:5000/isuser', {
            method: "POST",
            body: data
        }).then(response => response.json()).then(res => { if(res==='TRUE'){return true} else return false }).catch(err => console.log(err));
    }
    const username=useRef(null)
    const [title,setTitle]=useState('Choose a username')
    async function handleUsernameSubmit(){
        //to do - fetch backend to verify if user exists or not
        //switch current section on success
        let val=username.current.value
        let res=await fetchuser(val)
        if(!val)
            return
        else if(res){
            alert('User exists')
            return
        }
        
        setTitle('Record your voice')
        setCurr(<Recorder username={val} method={'register'}/>)
    }
    const usernameSection=(<div className={styles.inputsection}>
        <input ref={username} placeholder='Enter a username'/>
        <button onClick={handleUsernameSubmit}>Next</button>
    </div>)
    const [curr,setCurr]=useState(usernameSection)
    return <>
        <Head>
            <title>Register</title>
            <meta name="description" content="VBA7 registration page" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <link rel="icon" href="/favicon.ico" />
        </Head>
        <main className={styles.main}>
            <div className={styles.description}>
                <div>
                    {title}
                </div>
            </div>
            {curr}
        </main>
    </>
}