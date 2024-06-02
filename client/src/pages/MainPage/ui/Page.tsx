import { Ticker } from '@/features/Ticker';
import { tickerData } from '@/features/Ticker/data/data';
import { Opacity } from '@/shared/ui/Opacity';
import styles from './Page.module.scss';
import { AboutBlock } from './blocks/AboutBlock';
import { ImageBlock } from './blocks/ImageBlock';
import { Residents } from './blocks/Residents';

export default function MainPage() {
    return (
        <div className={styles.page}>
            <ImageBlock />
            <div className={styles.page__content} id="page">
                <Ticker
                    data={tickerData}
                />
                <Opacity>
                    <AboutBlock />
                </Opacity>
                <Opacity>
                    <Residents />
                </Opacity>
            </div>
        </div>
    )
}