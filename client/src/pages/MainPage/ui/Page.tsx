import { Ticker } from '@/features/Ticker';
import { AboutBlock } from './blocks/AboutBlock';
import { Residents } from './blocks/Residents';
import { tickerData } from '@/features/Ticker/type/data';
import styles from './Page.module.scss';
import { ImageBlock } from './blocks/ImageBlock';

export default function MainPage() {
    return (
        <div className={styles.page}>
            <ImageBlock />
            <Ticker
                data={tickerData}
            />
            <AboutBlock />
            <Residents />
        </div>
    )
}

//TODO: при загрузки ImageBlock убирать header по первого скролла