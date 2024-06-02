'use client'
import { Typewriter } from '@/widgets/Typewriter';
import { FC } from 'react';
import styles from './ImageBlock.module.scss';

interface ImageBlockProps {
    isVisibility: boolean;
}

export const ImageBlock: FC<ImageBlockProps> = (props) => {
    const {
        isVisibility,
    } = props;

    return (
        isVisibility ? (
            <div className={styles.image}>
                <Typewriter
                    text='Добро пожаловать!'
                    className={styles.typewriter}
                />
            </div>
        ) : null
    )
};