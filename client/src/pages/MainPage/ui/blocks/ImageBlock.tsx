import { Typewriter } from '@/widgets/Typewriter';
import styles from './ImageBlock.module.scss';

export const ImageBlock = () => {
    return (
        <div className={styles.image}>
            <Typewriter
                text='Добро пожаловать!'
                className={styles.typewriter}
            />
        </div>
    )
};