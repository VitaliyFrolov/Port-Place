'use client'
import { Ticker } from '@/features/Ticker';
import { tickerData } from '@/features/Ticker/data/data';
import { Opacity } from '@/shared/ui/Opacity';
import React, { useState } from 'react';
import { AboutBlock } from '../blocks/AboutBlock';
import { ImageBlock } from '../blocks/ImageBlock';
import { ResidentsBlock } from '../blocks/Residents';
import styles from './Page.module.scss';

const MainPage: React.FC = () => {
    const [isVisibility, setIsVisibility] = useState<boolean>(false);

    return (
        <div className={styles.page}>
            <ImageBlock
                isVisibility={isVisibility}
            />
            <div className={styles.page__content} id="page">
                <Ticker
                    data={tickerData}
                />
                <Opacity>
                    <AboutBlock />
                </Opacity>
                <Opacity>
                    <ResidentsBlock />
                </Opacity>
            </div>
        </div>
    );
}

export default MainPage;