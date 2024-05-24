import { FC } from 'react';
import styles from './Typewriter.module.scss';

interface TypewriterProps {
    text: string;
    width?: number;
}

export const Typewriter: FC<TypewriterProps> = (props) => {
    const {
        text,
    } = props;

    return (
        <div className={styles.text}>
            {text}
        </div>
    )
};

//FIXME: Поправить каретку