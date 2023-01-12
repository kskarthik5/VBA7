import Head from 'next/head'
import { Inter } from '@next/font/google'
import styles from '../styles/Home.module.css'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>VBA7 Demo</title>
        <meta name="description" content="A demonstration of a voice based authentication system" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <div className={styles.description}>
          <div>
            {'Voice Based Authentication System'}

          </div>
        </div>
        <div className={styles.grid}>
          <a
            href="/login"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Test <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Test out authentication using your registered voice
            </p>
          </a>

          <a
            href="/register"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Register <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Register your voice in the system
            </p>
          </a>

          
        </div>
      </main>
    </>
  )
}
