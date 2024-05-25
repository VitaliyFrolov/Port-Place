import { Ticker } from '@/features/Ticker';
import { AboutBlock } from './blocks/AboutBlock';
import { Residents } from './blocks/Residents';
import { tickerData } from '@/features/Ticker/data/data';
import { ImageBlock } from './blocks/ImageBlock';
import styles from './Page.module.scss';
import { Opacity } from '@/shared/ui/Opacity';

export default function MainPage() {
    return (
        <div className={styles.page}>
            <ImageBlock />
            <Ticker
                data={tickerData}
            />
            <Opacity>
                <AboutBlock />
            </Opacity>
            <Residents />
        </div>
    )
}